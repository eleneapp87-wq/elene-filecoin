# elene-filecoin

Open-source Filecoin storage client for Elene — a zero-knowledge consumer cloud storage app. 30% of all user data is written to Filecoin via S3-compatible API (Fil One).

## Architecture

- Shard Splitter — splits encrypted blobs into 10/60/30 tiers
- Filecoin Writer — writes cold-tier shards to Fil One (S3 API)
- Retrieval Client — fetches + decrypts cold-tier files on demand

## Stack

- Python 3.11+
- boto3 (S3-compatible to Fil One endpoint)
- AES-256-GCM (client-side encryption)
- BLAKE3 (file hashing)

## Milestones

- [x] Repo + architecture
- [ ] S3 write pipeline to Fil One
- [ ] Shard splitting logic (10/60/30)
- [ ] Retrieval + decrypt client
- [ ] 1,000 users storing data on Filecoin

## License

MIT + Apache 2.0 dual-licensed.   
