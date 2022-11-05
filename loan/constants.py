import uuid
from datetime import date, timedelta

loans = [
    {
        "uuid": str(uuid.uuid4()),
        "name": "ICICI VALUE-X01",
        "logo": "https://dailynewspk.com/wp-content/uploads/2020/12/ICICI-Bank-1024x640.jpg",
        "value": "40000",
        "due_date": str(date.today() + timedelta(days=10))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "HDFC MSME-R45",
        "logo": "https://imgs.search.brave.com/S7Hb1R33jYdHnjvFVuPmbYJqBmKyyT-iLcYwNHEyvLI/rs:fit:640:480:1/g:ce/aHR0cHM6Ly93d3cu/aGluZHVzdGFudGlt/ZXMuY29tL3JmL2lt/YWdlX3NpemVfNjQw/eDM2Mi9IVC9wMi8y/MDE2LzA0LzIyL1Bp/Y3R1cmVzL2hkZmMt/YmFuay1sb2dvLW9m/aWNpYWwtd2ViaXN0/ZV85ZWJlZmI0Ni0w/OGI2LTExZTYtYWZj/ZS1jZDU5MDg3NGM2/N2UuanBn",
        "value": "24000",
        "due_date": str(date.today() + timedelta(days=14))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "IDFC FIRST T50",
        "logo": "https://imgs.search.brave.com/1Rwm5mn34jRwJsrBYmAEb2SV6pc54pDUrt5Xjk5vX1k/rs:fit:1200:900:1/g:ce/aHR0cHM6Ly9jZG4u/c2lhc2F0LmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvMjAyMC8w/NS9JREZDLUZpcnN0/LUJhbmsuanBn",
        "value": "37499",
        "due_date": str(date.today() + timedelta(days=21))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "HDFC MIL T23",
        "logo": "https://imgs.search.brave.com/S7Hb1R33jYdHnjvFVuPmbYJqBmKyyT-iLcYwNHEyvLI/rs:fit:640:480:1/g:ce/aHR0cHM6Ly93d3cu/aGluZHVzdGFudGlt/ZXMuY29tL3JmL2lt/YWdlX3NpemVfNjQw/eDM2Mi9IVC9wMi8y/MDE2LzA0LzIyL1Bp/Y3R1cmVzL2hkZmMt/YmFuay1sb2dvLW9m/aWNpYWwtd2ViaXN0/ZV85ZWJlZmI0Ni0w/OGI2LTExZTYtYWZj/ZS1jZDU5MDg3NGM2/N2UuanBn",
        "value": "10999",
        "due_date": str(date.today() + timedelta(days=30))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "ICICI VALUE-X01",
        "value": "40000",
        "logo": "https://dailynewspk.com/wp-content/uploads/2020/12/ICICI-Bank-1024x640.jpg",
        "due_date": str(date.today() + timedelta(days=10))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "PNB PRO MSME-R45",
        "logo": "https://imgs.search.brave.com/Eac_vpCKdG2P3RwfvDu-dbHetDIaGgyQL2QxJVkRfoU/rs:fit:1200:720:1/g:ce/aHR0cHM6Ly9jZG4u/ZG5haW5kaWEuY29t/L3NpdGVzL2RlZmF1/bHQvZmlsZXMvc3R5/bGVzL2Z1bGwvcHVi/bGljLzIwMTYvMDEv/MDIvNDEwNTc5LXBu/Yi5qcGc",
        "value": "24000",
        "due_date": str(date.today() + timedelta(days=14))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "SBI SAFAR T50",
        "logo": "https://imgs.search.brave.com/TBL07c8jDrzGB4psvma01d9pMo3kbZqXJWxo46bue1k/rs:fit:1149:591:1/g:ce/aHR0cDovL3BuZ2lt/YWdlc2ZyZWUuY29t/L0xPR08vUy9zYmkt/YmFuay9TQkktTG9n/by1WRUNUT1ItQ0RS/LnBuZw",
        "value": "37499",
        "due_date": str(date.today() + timedelta(days=21))
    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "IDFC T23",
        "value": "10999",
        "logo": "https://imgs.search.brave.com/1Rwm5mn34jRwJsrBYmAEb2SV6pc54pDUrt5Xjk5vX1k/rs:fit:1200:900:1/g:ce/aHR0cHM6Ly9jZG4u/c2lhc2F0LmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvMjAyMC8w/NS9JREZDLUZpcnN0/LUJhbmsuanBn",
        "due_date": str(date.today() + timedelta(days=30))
    }
]

txns = [
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
        "type": "debit",
        "due_date": str(date.today() - timedelta(days=4)),

    },
    {
        "uuid": str(uuid.uuid4()),
        "name": "Laxman Kirana Store",
        "gstn": "06***********A4",
        "type": "credit",
        "value": 18999,
        "due_date": str(date.today() - timedelta(days=3)),

    }
]


offers = [
    {
        "id": 1,
        "name": "ICICI VALUE-X01",
        "interest": "6.5%",
        "logo": "https://dailynewspk.com/wp-content/uploads/2020/12/ICICI-Bank-1024x640.jpg",
        "ratings": "4/5"
    }, {
        "id": 2,
        "name": "HDFC MSME-R45",
        "logo": "https://imgs.search.brave.com/S7Hb1R33jYdHnjvFVuPmbYJqBmKyyT-iLcYwNHEyvLI/rs:fit:640:480:1/g:ce/aHR0cHM6Ly93d3cu/aGluZHVzdGFudGlt/ZXMuY29tL3JmL2lt/YWdlX3NpemVfNjQw/eDM2Mi9IVC9wMi8y/MDE2LzA0LzIyL1Bp/Y3R1cmVzL2hkZmMt/YmFuay1sb2dvLW9m/aWNpYWwtd2ViaXN0/ZV85ZWJlZmI0Ni0w/OGI2LTExZTYtYWZj/ZS1jZDU5MDg3NGM2/N2UuanBn",
        "interest": "7.1%",
        "ratings": "3.5/5"
    }, {
        "id": 3,
        "name": "IDFC FIRST T50",
        "logo": "https://imgs.search.brave.com/1Rwm5mn34jRwJsrBYmAEb2SV6pc54pDUrt5Xjk5vX1k/rs:fit:1200:900:1/g:ce/aHR0cHM6Ly9jZG4u/c2lhc2F0LmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvMjAyMC8w/NS9JREZDLUZpcnN0/LUJhbmsuanBn",
        "interest": "7.3%",
        "ratings": "3/5"
    }, {
        "id": 4,
        "name": "HDFC MIL T23",
        "logo": "https://imgs.search.brave.com/S7Hb1R33jYdHnjvFVuPmbYJqBmKyyT-iLcYwNHEyvLI/rs:fit:640:480:1/g:ce/aHR0cHM6Ly93d3cu/aGluZHVzdGFudGlt/ZXMuY29tL3JmL2lt/YWdlX3NpemVfNjQw/eDM2Mi9IVC9wMi8y/MDE2LzA0LzIyL1Bp/Y3R1cmVzL2hkZmMt/YmFuay1sb2dvLW9m/aWNpYWwtd2ViaXN0/ZV85ZWJlZmI0Ni0w/OGI2LTExZTYtYWZj/ZS1jZDU5MDg3NGM2/N2UuanBn",
        "interest": "6.1%",
        "ratings": "4.2/5"
    }, {
        "id": 5,
        "name": "PNB PRO MSME-R45",
        "logo": "https://imgs.search.brave.com/Eac_vpCKdG2P3RwfvDu-dbHetDIaGgyQL2QxJVkRfoU/rs:fit:1200:720:1/g:ce/aHR0cHM6Ly9jZG4u/ZG5haW5kaWEuY29t/L3NpdGVzL2RlZmF1/bHQvZmlsZXMvc3R5/bGVzL2Z1bGwvcHVi/bGljLzIwMTYvMDEv/MDIvNDEwNTc5LXBu/Yi5qcGc",
        "interest": "6%",
        "ratings": "4.8/5"
    },
]
