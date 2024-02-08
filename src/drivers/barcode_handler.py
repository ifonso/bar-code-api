from barcode import Code128
from barcode.writer import ImageWriter


# Here we use a design pattern called facade
class BarcodeHandler:

    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f"{tag}"
        tag.save(path_from_tag)

        return path_from_tag
