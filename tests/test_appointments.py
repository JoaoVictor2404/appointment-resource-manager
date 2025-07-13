def test_appointments_flow(client):
    client.post("/users/", json={"email":"x@y.com","password":"pwd"})
    tk = client.post("/token", data={"username":"x@y.com","password":"pwd"}).json()["access_token"]
    h = {"Authorization": f"Bearer {tk}"}
    client.post("/resources/", json={"name":"Equip","type":"Equip"}, headers=h)
    ap = {"title":"Teste","start":"2025-07-20T10:00:00","end":"2025-07-20T11:00:00","resource_id":1}
    resp = client.post("/appointments/", json=ap, headers=h)
    assert resp.status_code == 200 and resp.json()["title"]=="Teste"
