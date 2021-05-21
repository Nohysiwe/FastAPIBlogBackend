import uvicorn



uvicorn.run(
    "startBlogApp:BlogApp",
    host = "0.0.0.0",
    port = 7916,
)
