from textx import metamodel_from_file


class BaseMixin:
    def create_data(self) -> None:
        ocl_meta = metamodel_from_file("ocl.tx")
        self.example_model = ocl_meta.model_from_file("ocl.example")           

class AcceptanceOCLTestCase(BaseMixin):
    def main(self):
        self.create_data(self)
        ocl_meta = metamodel_from_file("ocl.tx")
        self.example_model = ocl_meta.model_from_file("ocl.example")            
        print(self.example_model.context[0].name)
        print(self.example_model.condition.name)



if __name__ == '__main__':
    AcceptanceOCLTestCase.main(AcceptanceOCLTestCase)  # pragma: no cover