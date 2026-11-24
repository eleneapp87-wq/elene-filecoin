# Architecture

Elene uses a 3-tier storage split:
- Hot (10%): Cloudflare R2 — last 30 days
- Warm (60%): Backblaze B2 — 30-180 days
- Cold (30%): Filecoin / Fil One — 180+ days

This repo contains the open-source Filecoin client layer only.
The full app (Flutter, Supabase, ads) is proprietary.   
