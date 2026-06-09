from segment_anything import sam_model_registry

checkpoint = "sam_vit_h.pth"
model_type = "vit_h"

sam = sam_model_registry[model_type](checkpoint=checkpoint)

print("SAM LOADED SUCCESSFULLY")