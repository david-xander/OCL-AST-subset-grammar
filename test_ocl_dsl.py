from textx import metamodel_from_file
import unittest


class BaseMixin(unittest.TestCase):
    def create_data(self) -> None:
        ocl_meta = metamodel_from_file("ocl.tx")
        self.example_model1 = ocl_meta.model_from_file("ocl.example")           
        self.example_model2 = ocl_meta.model_from_file("ocl2.example")           
        self.example_model3 = ocl_meta.model_from_file("ocl3.example")           
        self.example_model4 = ocl_meta.model_from_file("ocl4.example")           
        self.example_model5 = ocl_meta.model_from_file("ocl5.example")           


class AcceptanceOCLTestCase(BaseMixin):

    def setUp(self) -> None:
        self.create_data()

    def test_context(self):
        self.assertEqual("Person", self.example_model1.context[0].targetClass[0].name)

    def test_condition(self):
        self.assertEqual("inv", self.example_model1.lines[0].condition)

    def test_model_attribute(self):
        self.assertEqual("self", self.example_model1.lines[0].expression.left.atributeContext[0].targetClass.name)
        self.assertEqual("age", self.example_model1.lines[0].expression.left.attribute)

    def test_model_operator(self):
        self.assertEqual(">=", self.example_model1.lines[0].expression.operator)

    def test_model_value(self):
        self.assertEqual(18, self.example_model1.lines[0].expression.right)

    def test_model_value_oclexpression(self):
        self.assertEqual("registryCertificateDate", self.example_model2.lines[0].expression.left.attribute)
        self.assertEqual(">", self.example_model2.lines[0].expression.operator)
        self.assertEqual("birthDate", self.example_model2.lines[0].expression.right.attribute)

    def test_model_no_context(self):
        with self.assertRaises(AttributeError):
            # No debe existir este atributo si no se define un contexto
            cosa = self.example_model3.expression.context
        self.assertEqual("Person", self.example_model3.lines[0].expression.left.atributeContext[0].targetClass.name)
        self.assertEqual("registryCertificateDate", self.example_model3.lines[0].expression.left.attribute)
        self.assertEqual(">", self.example_model3.lines[0].expression.operator)
        self.assertEqual("birthDate", self.example_model3.lines[0].expression.right.attribute)

    def test_model_precondition_postcondition_contextMethodWithVar(self):
        self.assertEqual("Person", self.example_model4.context[0].targetClass[0].name)
        self.assertEqual("setAge", self.example_model4.context[0].classMethod[0].name)
        self.assertEqual("newAge", self.example_model4.context[0].classMethod[0].vars[0].name)
        self.assertEqual("int", self.example_model4.context[0].classMethod[0].vars[0].type)
        self.assertEqual("pre", self.example_model4.lines[0].condition)
        self.assertEqual("post", self.example_model4.lines[1].condition)

    def test_model_context_method_no_var(self):
        self.assertEqual("Person", self.example_model5.context[0].targetClass[0].name)
        self.assertEqual("getName", self.example_model5.context[0].classMethod[0].name)
        self.assertEqual([], self.example_model5.context[0].classMethod[0].vars)
        self.assertEqual("post", self.example_model5.lines[0].condition)



    def tearDown(self) -> None:
        super().tearDown()


if __name__ == '__main__':
    unittest.main()  # pragma: no cover