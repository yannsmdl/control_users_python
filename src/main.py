import asyncio
import hypercorn.asyncio
from config.main_inject import register_ioc
from routes import router
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html


load_dotenv()
app = FastAPI()

app.include_router(router)

# Função para gerar o esquema OpenAPI personalizado
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    # Definindo o esquema de segurança Bearer Token
    openapi_schema = get_openapi(
        title="Your API Title",
        version="1.0.0",
        description="Your API Description",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Rota para servir a documentação do Swagger UI
@app.get("/docs", include_in_schema=False, response_class=HTMLResponse)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Your API Docs"  # Caminho para o seu arquivo CSS personalizado
    )

# Rota para servir a documentação OpenAPI em JSON
@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return custom_openapi()


if __name__ == "__main__":
    register_ioc()
    asyncio.run(hypercorn.asyncio.serve(app, config=hypercorn.Config.from_mapping({"bind": "0.0.0.0:40050"})))

