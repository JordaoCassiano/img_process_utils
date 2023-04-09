import json

def convert_coco_to_edge_impulse(coco_file_path):
    with open(coco_file_path, 'r') as f:
        coco_data = json.load(f)

    edge_impulse_data = {
        "version": 1,
        "type": "bounding-box-labels",
        "boundingBoxes": {}
    }

    for image in coco_data['images']:
        filename = image['file_name']
        annotations = []

        for annotation in coco_data['annotations']:
            if annotation['image_id'] == image['id']:
                x, y, width, height = annotation['bbox']
                x = int(x)
                y = int(y)
                width = int(width)
                height = int(height)
                label = coco_data['categories'][annotation['category_id']]['name']

                annotation_data = {
                    "label": label,
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height
                }

                annotations.append(annotation_data)

        edge_impulse_data['boundingBoxes'][filename] = annotations

    with open('bounding_boxes.labels', 'w') as f:
        json.dump(edge_impulse_data, f)

    print('Conversion complete. File saved as "bounding_boxes.labels"')

# exemplo de uso
convert_coco_to_edge_impulse('_annotations.coco.json')
