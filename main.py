from app.searcher import buscar_web


def main():

    print("======================================")
    print("     MACHINING LEAD HUNTER")
    print("======================================")
    print()

    consulta = '"10000 pcs" "CNC machining" Mexico'

    print(f"Buscando: {consulta}")
    print()

    resultados = buscar_web(consulta)

    if not resultados:
        print("No se encontraron resultados.")
        return

    for i, resultado in enumerate(resultados, start=1):

        print(f"[{i}] {resultado['titulo']}")
        print(f"URL: {resultado['url']}")
        print(f"Descripción: {resultado['descripcion']}")
        print("-" * 70)


if __name__ == "__main__":
    main()