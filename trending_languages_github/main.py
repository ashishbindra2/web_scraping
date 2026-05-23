from fastapi import FastAPI
from github_scrab import github_treading_language, edges_extraction
# from file import python_dict


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/analyze/github/trending/{language}")
async def github_trending_lang(language: str):
    if not language:
        return {"Please provide a language "}
    
    url = f"https://github.com/trending/{language}"
    
    python_dict = {
        "nodes": [],
        "edges": []
        }
    
    for data in github_treading_language(url):
        print(data)
        python_dict["nodes"].append(data)

    for dt in python_dict["nodes"]: 
        for data in python_dict["nodes"]:
            temp = edges_extraction(dt["tags"],data["tags"])
            python_dict["edges"].append({"edges":dt['id'], "target":data['id'], "weight":len(temp)})
    

    return {"data":python_dict}








