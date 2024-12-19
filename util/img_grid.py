from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def create_transposed_grid_dynamic_labels(image_rows, row_labels, cols, image_size=(256, 256), save_path="output_grid.pdf"):
    """
    Creates a labeled grid with dynamic rows and columns, with centered text beside each row.
    Labels are dynamically sized based on the longest label.
    :param image_rows: List of lists, where each sublist contains image paths for a row.
    :param row_labels: List of row labels (header).
    :param cols: Number of columns of images.
    :param image_size: Tuple for image resizing (width, height).
    :param save_path: Path to save the output image.
    """
    rows = len(row_labels)
    if len(image_rows) != rows:
        raise ValueError("Number of rows in image_rows must match row_labels.")
    
    # Load and resize images
    resized_images = []
    for row in image_rows:
        resized_row = []
        for img_path in row[:cols]:
            try:
                img = Image.open(img_path).convert("RGB").resize(image_size)
                resized_row.append(img)
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")
                # Create a blank image as a placeholder
                resized_row.append(Image.new("RGB", image_size, "gray"))
        resized_images.append(resized_row)
    
    # Initialize font
    font_size = max(image_size[1] // 12, 12)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate maximum label width using font.getsize
    # Create a dummy image to initialize ImageDraw
    dummy_img = Image.new("RGB", (1, 1))
    dummy_draw = ImageDraw.Draw(dummy_img)
    label_widths = [dummy_draw.textbbox((0, 0), label, font=font)[2] for label in row_labels]
    max_label_width = max(label_widths) if label_widths else 0
    text_width = max_label_width + 20  # Add padding
    
    # Grid dimensions
    grid_width = cols * image_size[0] + text_width
    grid_height = rows * image_size[1]
    
    # Create a blank canvas
    grid_img = Image.new("RGB", (grid_width, grid_height), "white")
    draw = ImageDraw.Draw(grid_img)
    
    # Add centered row labels
    for i, label in enumerate(row_labels):
        # Calculate the bounding box of the text
        text_bbox = font.getbbox(label)
        label_width = text_bbox[2] - text_bbox[0]
        label_height = text_bbox[3] - text_bbox[1]
        
        # Calculate y position to center the text vertically within the row
        row_start_y = i * image_size[1]
        row_center_y = row_start_y + image_size[1] // 2
        
        # Calculate x position to center the text within the label area
        text_x = (text_width - label_width) // 2
        text_y = row_center_y - (label_height // 2)
        
        draw.text((text_x, text_y), label, fill="black", font=font)
    
    # Place images
    for row in range(rows):
        for col in range(cols):
            img = resized_images[row][col]
            x = text_width + col * image_size[0]
            y = row * image_size[1]
            grid_img.paste(img, (x, y))
    
    # Save and show the result
    grid_img.save(save_path)
    plt.figure(figsize=(cols * 3 + 3, rows * 3))
    plt.imshow(grid_img)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    cnt_num_list = [19, 9, 1, 14]
    sty_num_list = [38, 5, 16, 21]
    cnt_path = "data/cnt"
    sty_path = "data/sty"

    advdm_none = "output/sty"
    advdm_pgd = "output/sty_atk_16_100_512_1_2_1_0_0"
    advdm_mifgsm = "output/sty_mifgsm_16_100_512_1_2_1_0_0"
    advdm_vmifgsm = "output/sty_vmifgsm_16_100_512_1_2_1_0_0"

    rows = len(cnt_num_list)

    # Replace these file paths with your actual image paths
    content_images = [f"{cnt_path}/{(cnt_num)%20:02d}.png" for cnt_num in cnt_num_list]
    style_images = [f"{sty_path}/{(sty_num)%40:02d}.png" for sty_num in sty_num_list]
    advdm_none_images       = [f"{advdm_none}/{(cnt_num)%20:02d}_stylized_{(sty_num)%40:02d}.png" for cnt_num, sty_num in zip(cnt_num_list, sty_num_list)]
    advdm_pgd_images        = [f"{advdm_pgd}/{(cnt_num)%20:02d}_stylized_{(sty_num)%40:02d}.png" for cnt_num, sty_num in zip(cnt_num_list, sty_num_list)]
    advdm_mifgsm_images     = [f"{advdm_mifgsm}/{(cnt_num)%20:02d}_stylized_{(sty_num)%40:02d}.png" for cnt_num, sty_num in zip(cnt_num_list, sty_num_list)]
    advdm_vmifgsm_images    = [f"{advdm_vmifgsm}/{(cnt_num)%20:02d}_stylized_{(sty_num)%40:02d}.png" for cnt_num, sty_num in zip(cnt_num_list, sty_num_list)]

    # Combine all columns
    image_columns = [content_images, style_images, advdm_none_images, advdm_pgd_images, advdm_mifgsm_images, advdm_vmifgsm_images]
    column_labels = ["Content", "Style", "No Defense", "AdvDM(PGD)", "AdvDM(MIFGSM)", "AdvDM(VMIFGSM)"]

    # Create a dynamic grid with custom rows and columns
    create_dynamic_grid(image_columns, column_labels, rows, image_size=(256, 256))
    # create_transposed_grid_dynamic_labels(image_columns, column_labels, rows, image_size=(256, 256))


    # Replace these file paths with your own image file paths
    content_images = ["content1.jpg", "content2.jpg", "content3.jpg"]
    style_images = ["style1.jpg", "style2.jpg", "style3.jpg"]
    ours_images = ["ours1.jpg", "ours2.jpg", "ours3.jpg"]
    diffuseit_images = ["diffuse1.jpg", "diffuse2.jpg", "diffuse3.jpg"]
    inst_images = ["inst1.jpg", "inst2.jpg", "inst3.jpg"]
    diffstyle_images = ["diffstyle1.jpg", "diffstyle2.jpg", "diffstyle3.jpg"]