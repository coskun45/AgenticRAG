from dotenv import load_dotenv
from graph.graph import app
import os
load_dotenv()



if __name__ == '__main__':
    print(app.invoke(input={"question": "Nürnberg de hava nasil?"}))