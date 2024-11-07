
def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

if __name__ == "__main__":
    modified_dir = "../../data/practica_rag/harry_potter_books/_modified"
    embeddings_dir = "../../data/practica_rag/embeddings"

    os.makedirs(embeddings_dir, exist_ok=True)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    embeddings = []
    texts = []

    for filename in os.listdir(modified_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(modified_dir, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                splits = text_splitter.split_text(content)
                texts.extend(splits)

            split_embeddings = [None] * len(splits)

            # Generate embeddings using multithreading
            with ThreadPoolExecutor() as executor:
                future_to_index = {executor.submit(get_embedding, splits[i]): i for i in range(len(splits))}
                for future in tqdm(as_completed(future_to_index), total=len(splits), desc=f"Processing {filename}"):
                    index = future_to_index[future]
                    split_embeddings[index] = future.result()

            # Extend the main embeddings list with the ordered embeddings for this file
            embeddings.extend(split_embeddings)


    embeddings = np.array(embeddings)
    texts = np.array(texts)

    np.save(os.path.join(embeddings_dir, "embeddings.npy"), embeddings)
    np.save(os.path.join(embeddings_dir, "texts.npy"), texts)

    print("Embeddings saved and ready for search.")