# test.py modificado
def test_hamburguesa():
    ingrediente = "carne" # ¡ERROR INTENCIONADO!
    assert ingrediente == "carne", "¡Falta la carne en la hamburguesa!"
    print("Test superado: La hamburguesa tiene carne.")

if __name__ == "__main__":
    test_hamburguesa()
