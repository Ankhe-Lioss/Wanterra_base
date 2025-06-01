from PIL import Image
import numpy as np
import os
from scipy.ndimage import label, find_objects

# Load image
sprite_sheet = Image.open("needed to crop/terrain_atlas.png").convert("RGBA")
data = np.array(sprite_sheet)

# Create a mask of non-transparent pixels
alpha = data[:, :, 3]
mask = alpha > 0

# Label connected regions
labeled, num_features = label(mask)

# Get bounding boxes for each object
slices = find_objects(labeled)

# Output directory
output_dir = "objects_autocropped"
os.makedirs(output_dir, exist_ok=True)

count = 0
for i, obj_slice in enumerate(slices):
    if obj_slice is None:
        continue
    y_slice, x_slice = obj_slice
    cropped_image = sprite_sheet.crop((x_slice.start, y_slice.start, x_slice.stop, y_slice.stop))
    cropped_image.save(os.path.join(output_dir, f"object_{count}.png"))
    count += 1

print(f"Extracted {count} distinct objects to '{output_dir}/'")
