#!/usr/bin/env python
"""Example workflow: Create, edit, and save a JianYing draft"""
import requests
import time

BASE_URL = "http://127.0.0.1:12402"

print("=" * 60)
print("Complete Draft Creation Workflow")
print("=" * 60)

# Step 1: Create a new draft
print("\n📝 Step 1: Creating a new draft...")
response = requests.post(f"{BASE_URL}/create_draft", json={
    "width": 1080,
    "height": 1920
})
result = response.json()
if result['success']:
    draft_id = result['output']['draft_id']
    draft_url = result['output']['draft_url']
    print(f"✅ Draft created successfully!")
    print(f"   Draft ID: {draft_id}")
    print(f"   Draft URL: {draft_url}")
else:
    print(f"❌ Failed to create draft: {result['error']}")
    exit(1)

# Step 2: Add a video clip
print("\n🎬 Step 2: Adding a video clip...")
response = requests.post(f"{BASE_URL}/add_video", json={
    "draft_id": draft_id,
    "video_url": "https://cdn.wanx.aliyuncs.com/wanx/1719234057367822001/text_to_video/092faf3c94244973ab752ee1280ba76f.mp4",
    "start": 0,
    "end": 5,
    "width": 1080,
    "height": 1920,
    "track_name": "main"
})
result = response.json()
if result['success']:
    print(f"✅ Video added successfully!")
else:
    print(f"❌ Failed to add video: {result['error']}")

# Step 3: Add text
print("\n📝 Step 3: Adding text overlay...")
response = requests.post(f"{BASE_URL}/add_text", json={
    "draft_id": draft_id,
    "text": "Hello from CapCut API!",
    "start": 0,
    "end": 5,
    "font": "思源中宋",
    "font_color": "#FFFFFF",
    "font_size": 30.0,
    "track_name": "text_main",
    "transform_y": -0.7
})
result = response.json()
if result['success']:
    print(f"✅ Text added successfully!")
else:
    print(f"❌ Failed to add text: {result['error']}")

# Step 4: Save the draft
print("\n💾 Step 4: Saving draft to disk...")
print("   (This will download all media files...)")

# For macOS JianyingPro
draft_folder = "/Users/chenhh/Movies/JianyingPro/User Data/Projects/com.lveditor.draft"

response = requests.post(f"{BASE_URL}/save_draft", json={
    "draft_id": draft_id,
    "draft_folder": draft_folder
})
result = response.json()
if result['success']:
    print(f"✅ Draft saved successfully!")
    print(f"\n📂 Draft Location:")
    print(f"   Temporary: /Users/chenhh/projects/CapCutAPI/{draft_id}/")
    print(f"   Final: {draft_folder}/{draft_id}/")
    print(f"\n🎉 Next Steps:")
    print(f"   1. Copy the draft folder to JianyingPro:")
    print(f"      cp -r /Users/chenhh/projects/CapCutAPI/{draft_id} '{draft_folder}/'")
    print(f"   2. Open JianyingPro app")
    print(f"   3. Your draft should appear in the project list!")
else:
    print(f"❌ Failed to save draft: {result['error']}")

print("\n" + "=" * 60)

