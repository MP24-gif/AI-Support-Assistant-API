from fastapi import FastAPI, HTTPException
from groq import APIConnectionError, APITimeoutError, APIStatusError

from app.models import SupportRequest, SupportResponse
from app.llm import ask_model


app = FastAPI(
    title="AI Support Assistant API",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/support", response_model=SupportResponse)
async def support(request: SupportRequest):

    try:

        answer = ask_model(request.question)

        return {
            "success": True,
            "question": request.question,
            "answer": answer
        }

    except APITimeoutError:

        raise HTTPException(
            status_code=504,
            detail="The AI provider timed out. Please try again."
        )

    except APIConnectionError:

        raise HTTPException(
            status_code=503,
            detail="Unable to connect to the AI provider."
        )

    except APIStatusError:
        raise HTTPException(
        status_code=502,
        detail={
            "error": "model_provider_error",
            "message": "The AI provider returned an error."
        }
    )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unexpected server error."
        )
