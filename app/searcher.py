import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def buscar_web(query, num_resultados=10):

    url = f"https://html.duckduckgo.com/html/?q={quote(query)}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/151.0.0.0 Safari/537.36"
        )
    }

    try:

        respuesta = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        print(f"HTTP: {respuesta.status_code}")
        print(f"Tamaño respuesta: {len(respuesta.text)} caracteres")

        if respuesta.status_code != 200:
            print(respuesta.text[:500])
            return []

        soup = BeautifulSoup(respuesta.text, "html.parser")

        resultados = []

        for resultado in soup.select(".result"):

            titulo = resultado.select_one(".result__title a")
            descripcion = resultado.select_one(".result__snippet")

            if not titulo:
                continue

            resultados.append({
                "titulo": titulo.get_text(" ", strip=True),
                "url": titulo.get("href"),
                "descripcion": (
                    descripcion.get_text(" ", strip=True)
                    if descripcion
                    else ""
                )
            })

            if len(resultados) >= num_resultados:
                break

        return resultados

    except requests.RequestException as e:

        print(f"Error de conexión: {e}")

        return []