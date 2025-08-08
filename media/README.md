# Media Files Directory

This directory contains photos and videos of road conditions in the Bedian Road & Ali View Garden area that will be automatically attached to emails.

## 🚀 Automatic File Discovery

The system now **automatically discovers and validates** all media files in this directory. You don't need to specify filenames - just add your files and they'll be included!

## 📁 Supported File Types

### Images
- **JPG/JPEG** - Photos of road conditions, potholes, flooding
- **PNG** - Screenshots, diagrams, maps
- **GIF** - Animated images
- **BMP** - Bitmap images
- **TIFF** - High-quality photos
- **WebP** - Modern web images

### Videos
- **MP4** - Most common video format
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
- **System will automatically**: Stop adding files when limit is reached

## 📋 How to Add Files

1. **Take photos/videos** of road conditions
2. **Save them** in this `media/` directory
3. **Use any filename** - the system will find them automatically
4. **Supported formats only** - see list above
5. **Check file sizes** - keep under 25MB each

## 🎯 Recommended Content

### Photos to Include
- **Potholes and road damage**
- **Flooding and drainage issues**
- **Street lighting problems**
- **Traffic congestion**
- **Vehicle damage from road conditions**
- **Comparison with better-maintained areas**

### Videos to Include
- **Driving through potholes**
- **Flooding during rain**
- **Traffic jams due to road conditions**
- **Emergency vehicles struggling**
- **Time-lapse of deteriorating conditions**

### Documents to Include
- **Official complaints filed**
- **Damage estimates**
- **Medical reports (if injuries)**
- **Vehicle repair bills**
- **Maps showing affected areas**

## ⚠️ File Validation

The system automatically checks each file:

### ✅ What Gets Included
- Files with supported extensions
- Files under 25MB each
- Files that don't exceed 50MB total
- Non-hidden files (not starting with '.')

### ❌ What Gets Skipped
- Unsupported file types
- Files over 25MB
- Files that would exceed 50MB total
- Hidden files and directories
- Corrupted or unreadable files

## 📊 Example File Structure

```
media/
├── road_damage_photo1.jpg      ✅ Included
├── flooding_video.mp4          ✅ Included
├── pothole_documentation.pdf   ✅ Included
├── traffic_jam_photo.png       ✅ Included
├── oversized_video.mov         ❌ Too large (>25MB)
├── unsupported_file.psd        ❌ Unsupported format
├── .hidden_file.txt            ❌ Hidden file
└── README.md                   ❌ Not a media file
```

## 🔧 Troubleshooting

### Files Not Being Attached?
1. **Check file extension** - must be in supported list
2. **Check file size** - must be under 25MB
3. **Check total size** - all files must fit under 50MB
4. **Check file permissions** - must be readable

### Email Too Large?
1. **Compress videos** - use MP4 with H.264 codec
2. **Resize photos** - 1920x1080 is usually sufficient
3. **Reduce quality** - 80% JPEG quality is often fine
4. **Split into multiple emails** - if you have many files

### Performance Issues?
1. **Use efficient formats** - MP4 for video, JPEG for photos
2. **Optimize file sizes** - compress before adding
3. **Limit number of files** - 5-10 files per email is ideal

## 📈 Best Practices

1. **Use descriptive filenames** - helps with organization
2. **Include timestamps** - shows when photos were taken
3. **Document locations** - include street names in filenames
4. **Regular updates** - add new photos as conditions change
5. **Quality over quantity** - better to have fewer, high-quality files

## 🎉 You're Ready!

Simply add your media files to this directory and the system will:
- ✅ Automatically discover all valid files
- ✅ Validate file types and sizes
- ✅ Attach them to daily emails
- ✅ Skip invalid or oversized files
- ✅ Provide detailed logging of what's included

**No configuration needed - just add your files!**
