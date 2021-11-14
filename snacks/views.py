from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    snacks = {
        "a": {
            "name":"M&M's",
            "about": "M&M's are multi-colored button-shaped chocolates, each of which has the letter \"m\" printed in lower case in white on one side, consisting of a candy shell surrounding a filling which varies depending upon the variety of M&M's.",
            "img": "https://japee.tokyo/wp-content/uploads/2019/03/4902397840558.jpg"
        },
        "b": {
            "name": "Doritos",
            "about": "Doritos is an American brand of flavored tortilla chips produced since 1964 by Frito-Lay, a wholly owned subsidiary of PepsiCo.",
            "img": "https://scene7.samsclub.com/is/image/samsclub/0002840044375_B?wid=400&hei=400"
        },
        "c": {
            "name":"Snickers",
            "about": "Snickers is a chocolate bar made by the American company Mars, Incorporated, consisting of nougat topped with caramel and peanuts that has been enrobed in milk chocolate.",
            "img": "https://5.imimg.com/data5/SELLER/Default/2020/8/LN/LI/GI/112052042/chocolate-500x500.jpeg"
        },
        "d": {
            "name": "Hershey's",
            "about": "The Hershey Company, commonly known as Hershey's, is an American multinational company and one of the largest chocolate manufacturers in the world.",
            "img": "https://www.candywarehouse.com/item-images/133730-01_hersheys-1-pound-chocolate-bar.jpg?resizeid=102&resizeh=500&resizew=500"
        },
        "e": {
            "name": "Maltesers",
            "about": "Maltesers are a British confectionery product manufactured by Mars, Incorporated. First sold in the UK in 1937, they were originally aimed at women. They have since been sold in Europe, Australia, New Zealand, Canada, and, since 2017, the US. The slogan is \"The lighter way to enjoy chocolate\".",
            "img": "https://www.crazyprotein.com/todocad/2021/10/maltesers-protein-powder-milk-chocolate-malt-450-g-1-1.jpeg"
        },
        "f": {
            "name": "Cheetos",
            "about": "Cheetos is a crunchy corn puff snack brand made by Frito-Lay, a subsidiary of PepsiCo. Fritos creator Charles Elmer Doolin invented Cheetos in 1948, and began national distribution in the U.S. ",
            "img": "https://d2d8wwwkmhfcva.cloudfront.net/800x/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_547ad9f5-cd64-4070-acc5-1217be988cf8.png"
        }
        
    }
    return render(request, 'snacks/home.html', content = {"snacks":snacks})

def about(request):
    return render(request, 'snacks/about.html')