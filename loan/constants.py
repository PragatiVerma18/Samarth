import uuid
from datetime import date, timedelta

loans = [
    {
        "uuid": str(uuid.uuid4()),
        "name": "ICICI VALUE-X01",
        "value": "40000",
        "due_date": str(date.today() + timedelta(days=10))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "HDFC MSME-R45",
        "value": "24000",
        "due_date": str(date.today() + timedelta(days=14))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "IDFC FIRST T50",
        "value": "37499",
        "due_date": str(date.today() + timedelta(days=21))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "HDFC MIL T23",
        "value": "10999",
        "due_date": str(date.today() + timedelta(days=30))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "ICICI VALUE-X01",
        "value": "40000",
        "due_date": str(date.today() + timedelta(days=10))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "PNB PRO MSME-R45",
        "value": "24000",
        "due_date": str(date.today() + timedelta(days=14))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "SBI SAFAR T50",
        "value": "37499",
        "due_date": str(date.today() + timedelta(days=21))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "IDFC T23",
        "value": "10999",
        "due_date": str(date.today() + timedelta(days=30))
    }
]

txns =[
    {
        "uuid": str(uuid.uuid4()),
        "name": "Laxman Kirana Store",
        "gstn": "06***********A4",
        "value": 18999,
        "type": "credit",
        "due_date": str(date.today() - timedelta(days=1)),
        
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "Agrawal General Store",
        "gstn": "06***********M7",
        "value": 12500,
        "type": "credit",
        "due_date": str(date.today() - timedelta(days=2)),
        
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "Abhirup Kirana Store",
        "gstn": "06***********D1",
        "value": 25000,
        "type": "credit",
        "due_date": str(date.today() - timedelta(days=3)),
        
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "Mahesh ITC sales",
        "gstn": "06***********I5",
        "value": 65000,
        "type": "debit",
        "due_date": str(date.today() - timedelta(days=4)),
        
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "Abhishek PnG Retails",
        "gstn": "03***********T4",
        "value": 71000,
        "type": "debit",
        "due_date": str(date.today() - timedelta(days=5)),
        
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "PEPSICO SALES",
        "gstn": "03***********A3",
        "value": 18999,
        "due_date": str(date.today() - timedelta(days=4)),
        
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "Laxman Kirana Store",
        "gstn": "06***********A4",
        "value": 18999,
        "due_date": str(date.today() - timedelta(days=3)),
        
    }
]


offers =[
    {
        "id": 1,
        "name": "ICICI VALUE-X01",
        "interest": "6.5%",
        "ratings": "4/5"
    },{
        "id": 2,
        "name": "HDFC MSME-R45",
        "interest": "7.1%",
        "ratings": "3.5/5"
    },{
        "id": 3,
        "name": "IDFC FIRST T50",
        "interest": "7.3%",
        "ratings": "3/5"
    },{
        "id": 4,
        "name": "HDFC MIL T23",
        "interest": "6.1%",
        "ratings": "4.2/5"
    },{
        "id": 5,
        "name": "PNB PRO MSME-R45",
        "interest": "6%",
        "ratings": "4.8/5"
    },
]