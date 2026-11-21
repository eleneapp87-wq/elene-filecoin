"""Minimal Filecoin store & retrieve script using the lighthouseweb3 Python SDK."""

import os
from pathlib import Path
from lighthouseweb3 import Lighthouse


def main() -> None:
    # Load your Filecoin/Lighthouse API token from the environment
    token = os.environ.get("LIGHTHOUSE_TOKEN")
    if not token:
        raise RuntimeError("Set LIGHTHOUSE_TOKEN before running this script.")

    # Initialize the Filecoin storage client
    client = Lighthouse(token=token)

    # 1. Create a local text file to upload
    source_path = Path("sample.txt")
    source_path.write_text("Hello, Filecoin!", encoding="utf-8")

    # 2. Store the file on Filecoin/IPFS and extract its CID
    response = client.upload(source=str(source_path))
    cid = response["data"]["Hash"]
    print(f"Stored {source_path} -> CID: {cid}")

    # 3. Retrieve the file back from Filecoin/IPFS by CID
    content_bytes, _metadata = client.download(cid)

    # 4. Write the retrieved data locally and print it
    output_path = Path("retrieved_sample.txt")
    output_path.write_bytes(content_bytes)
    print(f"Retrieved content: {output_path.read_text(encoding='utf-8')}")


if __name__ == "__main__":
    main()   
