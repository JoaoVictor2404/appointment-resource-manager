def test_register_and_login(client):
    res = client.post("/users/", json={"email":"a@b.com","password":"123456"})
    assert res.status_code == 200
    res2 = client.post("/token", data={"username":"a@b.com","password":"123456"})
    assert "access_token" in res2.json()
