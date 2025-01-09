from pygrocytoo.data_models.product import ProductBarcode
from pygrocytoo.grocy_api_client import ProductBarcodeData


class TestMisc:
    def test_158_productbarcode_deserialization(self):
        parsed_data = {"barcode": "123"}
        data = ProductBarcodeData(**parsed_data)

        barcode = ProductBarcode(data)
        result = barcode.to_json()

        assert result is not None
        assert "barcode" in result
        assert "123" in result
