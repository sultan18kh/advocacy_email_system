# Media Files Directory

This directory contains photos and videos of road conditions in the Bedian Road & Ali View Garden area that will be automatically attached to emails.

## 🚀 Automatic File Discovery

The system **automatically discovers and validates** all media files in this directory. You don't need to specify filenames - just add your files with ANY descriptive names and they'll be included!

## 📁 Supported File Types (22+ Extensions)

### Images
- **JPG/JPEG** - Photos of road conditions, potholes, flooding
- **PNG** - Screenshots, diagrams, maps
- **GIF** - Animated images
- **BMP** - Bitmap images
- **TIFF** - High-quality photos
- **WebP** - Modern web images

### Videos
- **MP4** - Most common video format (recommended)
- **AVI** - Windows video format
- **MOV** - Apple video format
- **WMV** - Windows Media Video
- **FLV** - Flash video
- **WebM** - Web video format
- **MKV** - Matroska video

### Documents
- **PDF** - Reports, documents, maps
- **DOC/DOCX** - Word documents
- **TXT** - Text files
- **RTF** - Rich text files

### Archives
- **ZIP** - Compressed files
- **RAR** - Compressed archives
- **7Z** - 7-Zip archives

## 📏 File Size Limits

### Individual File Limits
- **Maximum file size**: 25MB per file
- **Recommended**: Under 10MB for faster email delivery

### Total Attachment Limits
- **Maximum total size**: 50MB per email
- **System behavior**: Automatically stops adding files when limit is reached

## 📋 How to Add Files

1. **Take photos/videos** of road conditions
2. **Save them** in this `media/` directory with ANY descriptive filename
3. **Use supported formats** - see list above
4. **Check file sizes** - keep under 25MB each
5. **That's it!** - System automatically finds and validates everything

## 🎯 Recommended Content & Naming

### Photos to Include
```
pothole_damage_bedian_road_jan2025.jpg
flooding_ali_view_garden_monsoon.png
street_lighting_broken_jan15_2025.jpg
traffic_jam_due_to_potholes.jpeg
vehicle_damage_from_potholes.jpg
comparison_dha_vs_bedian_roads.png
```

### Videos to Include
```
driving_through_potholes_bedian.mp4
flooding_during_rain_ali_view.mov
traffic_congestion_poor_roads.mp4
emergency_vehicle_struggling.avi
time_lapse_road_deterioration.mp4
```

### Documents to Include
```
official_complaint_filed_2025.pdf
vehicle_repair_estimate.docx
medical_report_accident.pdf
drainage_system_proposal.pdf
area_map_with_problems.pdf
```

## ⚠️ File Validation Process

The system automatically checks each file and provides detailed feedback:

### ✅ What Gets Included
- Files with supported extensions (22+ types)
- Files under 25MB each
- Files that don't cause total to exceed 50MB
- Non-hidden files (not starting with '.')
- Readable files with proper permissions

### ❌ What Gets Skipped (with reasons)
- Unsupported file types → "Skipping unsupported file type"
- Files over 25MB → "Skipping oversized file (X.X MB > 25MB)"
- Files that exceed total limit → "Total size limit reached"
- Hidden files (.hidden_file.txt) → Automatically ignored
- Corrupted or unreadable files → "Skipping unreadable file"

## 📊 Example File Discovery Output

When you run the system, you'll see detailed logging:

```
📁 Testing Media File Discovery...
✅ Supported file types: 22 extensions
✅ Media directory found: '../media'
✅ Valid media file: pothole_damage_jan2025.jpg (2.3MB)
✅ Valid media file: flooding_video_dec2024.mp4 (15.7MB)
✅ Valid media file: official_complaint.pdf (0.8MB)
⚠️  Skipping oversized file: large_video.mov (30.2MB > 25MB)
⚠️  Skipping unsupported file: design_file.psd
📁 Total valid media files: 3 (18.8MB)
📋 File size limits: Individual 25MB, Total 50MB
```

## 🔧 Path Resolution

The system intelligently finds the media directory using multiple strategies:

### ✅ Automatic Detection
1. **From src/**: `../media` (when running from src directory)
2. **From root**: `./media` (when running from project root)
3. **Current working directory**: `media/` (fallback)

### ✅ Robust Handling
- Uses `pathlib.Path` for cross-platform compatibility
- Handles different execution contexts (local vs GitHub Actions)
- Provides clear error messages if directory not found

## 🔧 Troubleshooting

### Files Not Being Discovered?
```bash
# Run the test to see file discovery in action
python src/test_email.py
```

**Check the output for:**
- "Media directory found" message
- List of valid files discovered
- Reasons for any skipped files

### Files Not Being Attached?
1. **Check file extension** - must be in supported list above
2. **Check file size** - must be under 25MB each
3. **Check total size** - all files must fit under 50MB total
4. **Check file permissions** - must be readable by the system
5. **Check filename** - avoid special characters, use descriptive names

### Email Too Large?
1. **Compress videos** - use MP4 with H.264 codec
2. **Resize photos** - 1920x1080 is usually sufficient
3. **Reduce quality** - 80% JPEG quality is often fine
4. **Use fewer files** - system will auto-stop at 50MB limit

### Performance Issues?
1. **Use efficient formats** - MP4 for video, JPEG for photos
2. **Optimize file sizes** - compress before adding
3. **Limit file count** - 5-10 files per email is ideal
4. **Use descriptive names** - helps with organization

## 📈 Best Practices

### Naming Conventions
- **Include dates**: `pothole_damage_2025_01_15.jpg`
- **Include locations**: `bedian_road_flooding.mp4`
- **Include descriptions**: `vehicle_damage_from_potholes.jpg`
- **Use underscores**: `traffic_jam_due_to_poor_roads.png`
- **Be descriptive**: `official_complaint_walton_cantonment.pdf`

### File Organization Tips
```
media/
├── photos/
│   ├── potholes_2025_01_15.jpg
│   ├── flooding_2025_01_20.jpg
│   └── street_lights_broken_2025_01_25.jpg
├── videos/
│   ├── driving_through_potholes_jan2025.mp4
│   └── flooding_during_rain_dec2024.mp4
└── documents/
    ├── official_complaint_jan2025.pdf
    └── vehicle_repair_estimate.docx
```

### Quality Guidelines
1. **High resolution** for photos (but compressed for email)
2. **Stable video** - avoid shaky footage when possible
3. **Good lighting** - take photos during daylight
4. **Clear documentation** - ensure damage is clearly visible
5. **Multiple angles** - show extent of problems

## 🎉 You're Ready!

Simply add your media files to this directory and the system will:
- ✅ **Automatically discover** all valid files with ANY filename
- ✅ **Validate file types** against 22+ supported extensions
- ✅ **Check file sizes** and total limits
- ✅ **Attach to emails** sent Mon/Wed/Fri
- ✅ **Provide detailed logging** of what's included/skipped
- ✅ **Handle errors gracefully** with clear explanations

**No configuration needed - just add your files with descriptive names!**

---

**Latest Update**: Enhanced automatic discovery with 22+ file types, robust path resolution, detailed validation feedback, and cross-platform compatibility.