class Car:

    def __init__(self,request):
        self.request = request
        self.session = request.session

        car = self.session.get("car")
        total = self.session.get("carTotal")
        if not car:
            car = self.session["car"] = {}
            total = self.session["carTotal"] = 0
        
        self.car = car
        self.total = total


    def add(self, product, cuantity):
        if str(product.id) not in self.car.keys():
            self.car[product.id]={
                "product_id": product.id,
                "name": product.name,
                "cuantity": cuantity,
                "price": str(product.price),
                
                "category": product.category.name,
                "total": str(cuantity * product.price)
            }
        else:
            #update product in car
            for key, value in self.car.items():
                if key == str(product.id):
                    value["cuantity"] = str(int(value["cuantity"]) + cuantity)
                    value["total"] = str(float(value["cuantity"]) * float(value["price"]))
                    break

        self.save()

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.car:
            del self.car[product_id]
            self.save()

    def clear(self):
        self.session["car"] = {}
        self.session["carTotal"] = 0

    def save(self):
        total = 0

        for key,value in self.car.items():
            total += float(value["total"])

        self.session["carTotal"] = total 
        self.session["car"] = self.car
        self.session.modified = True