# example-api
first api with python

primer app usando python, quiero realizar un microservicio que llame a un api externa y guarde cierta informacion en una db

Request → weatherController.py → service.py → repository.py → DB
                                           ↘ client.py → API externa -> DB

la idea: llamar el api de https://open-meteo.com/ y guardar en base de datos la informacion realacionada 


├── app
│   ├── dto
│   ├── entities
│   ├── main.py
│   ├── repositories
│   └── services