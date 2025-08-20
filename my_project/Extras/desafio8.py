while True:
    arquivos = ["relatorio.docx", "doc.docx", "atendimento.pdf", "planilha.xlsx", "resumo.txt"]
    doc = []
    pd = []

    input("")
    for i in arquivos:
        if i.endswith(".docx"):
            doc.append(i)
            docx = doc
        elif i.endswith(".pdf"):
            pd.append(i)
            pdf = pd

    print(arquivos)
    filtro = int(input("1 - filtrar pdf     2 - filtrar docx \n"))

    if filtro == 1:
        print(f"os pdfs sao: {pdf}")
    elif filtro == 2:
        print(f"os docx sao: {docx}")
    else:
        print("invalido")
        continue