from twttr import shorten


def test_twttr():
    assert shorten("hola")=="hl"
    assert shorten("Adios")=="ds"
    assert shorten("Helado")=="Hld"
    assert shorten("Mejor 123")=="Mjr 123"
    assert shorten("Mi nombre es, javier")=="M nmbr s, jvr"


if __name__ == "__main__":
    main()
