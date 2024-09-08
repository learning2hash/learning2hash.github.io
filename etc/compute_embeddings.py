import argparse
import json
import numpy as np
import torch
import sklearn.manifold
import transformers

def parse_arguments():
    parser = argparse.ArgumentParser(description="TSNE Visualization of Papers in ML4Code")
    parser.add_argument("json", default=False, help="the path to the JSON containing all papers.")
    parser.add_argument("outpath", default=False, help="the target path of the visualizations papers.")
    parser.add_argument("--seed", default=0, help="The seed for TSNE.", type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    # Load the tokenizer and model
    tokenizer = transformers.AutoTokenizer.from_pretrained("deepset/sentence_bert")
    model = transformers.AutoModel.from_pretrained("deepset/sentence_bert")
    model.eval()

    # Use GPU if available
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    with open(args.json) as f:
        data = json.load(f)

    print(f"Num papers: {len(data)}")

    all_embeddings = []

    # Process each paper's abstract
    for paper_info in data:
        with torch.no_grad():
            # Tokenize with truncation and pass in attention_mask (without clean_up_tokenization_spaces)
            inputs = tokenizer.encode_plus(
                paper_info["abstract"],
                padding='max_length', 
                truncation=True, 
                max_length=512,
                return_tensors="pt"
            )
            token_ids = inputs["input_ids"].to(device)
            attention_mask = inputs["attention_mask"].to(device)

            # Get hidden states and pass attention_mask to the model
            hidden_states = model(input_ids=token_ids, attention_mask=attention_mask)[0]  # Use last hidden layer
            all_embeddings.append(hidden_states.mean(1).squeeze().cpu().numpy())  # Mean pooling

    # Seed the random generator for reproducibility
    np.random.seed(args.seed)
    all_embeddings = np.array(all_embeddings)

    # Apply TSNE for dimensionality reduction
    out = sklearn.manifold.TSNE(n_components=2, metric="cosine").fit_transform(all_embeddings)

    # Store the resulting TSNE embeddings
    for i, paper_info in enumerate(data):
        paper_info['tsne_embedding'] = out[i].tolist()

    # Write the updated data with TSNE embeddings to the output path
    with open(args.outpath, 'w') as f:
        json.dump(data, f)
