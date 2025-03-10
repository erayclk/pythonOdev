from product import Product
from customer import Customer
from cart import Cart
from order import Order

def display_header():
    print("\n" + "="*50)
    print("\tE-TİCARET SİSTEMİ")
    print("="*50)

def main():
    products = [
        Product("Laptop", 15000, 10),
        Product("Telefon", 10000, 15),
        Product("Tablet", 5000, 20),
        Product("Kulaklık", 1000, 30),
        Product("Mouse", 500, 50)
    ]
    
    customer = Customer("Eray", "eray@yandex.com")
    cart = Cart()
    
    while True:
        display_header()
        print(f"\nHoş geldiniz, {customer.name}!")
        print(f"Sepetinizde {len(cart.items)} çeşit ürün bulunuyor.")
        if cart.items:
            print(f"Toplam Tutar: {cart.get_total()} TL")
        
        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("-"*40)
        print("1. Ürün Ekle")
        print("2. Ürün Çıkar")
        print("3. Sepeti Görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")
        print("-"*40)
        
        choice = input("\nSeçiminiz (1-5): ")
        
        if choice == "1":
            print("\n=== MEVCUT ÜRÜNLER ===")
            print("-"*40)
            for i, product in enumerate(products, 1):
                print(f"{i}. {product.name}")
                print(f"   Fiyat: {product.price} TL")
                print(f"   Stok: {product.stock} adet")
                print("-"*30)
            
            try:
                product_index = int(input("\nEklemek istediğiniz ürünün numarasını girin: ")) - 1
                if 0 <= product_index < len(products):
                    selected_product = products[product_index]
                    print(f"\nSeçilen ürün: {selected_product.name}")
                    print(f"Mevcut stok: {selected_product.stock}")
                    
                    quantity = int(input("Kaç adet eklemek istiyorsunuz?: "))
                    if quantity <= selected_product.stock:
                        cart.add_product(selected_product, quantity)
                        print(f"\n✓ {quantity} adet {selected_product.name} sepete eklendi!")
                        print(f"Güncel sepet tutarı: {cart.get_total()} TL")
                    else:
                        print("\n❌ Yetersiz stok! Lütfen daha az miktarda ürün seçin.")
                else:
                    print("\n❌ Geçersiz ürün numarası!")
            except ValueError:
                print("\n❌ Geçersiz giriş! Lütfen sayı giriniz.")
                
        elif choice == "2":
            if not cart.items:
                print("\n❌ Sepetiniz boş!")
                input("\nDevam etmek için Enter'a basın...")
                continue
                
            print("\n=== SEPETİNİZDEKİ ÜRÜNLER ===")
            cart.display_cart()
            print("-"*40)
            
            product_name = input("\nÇıkarmak istediğiniz ürünün adını girin: ")
            if product_name in cart.items:
                cart.remove_product(product_name)
                print(f"\n✓ {product_name} sepetten çıkarıldı!")
                print(f"Güncel sepet tutarı: {cart.get_total()} TL")
            else:
                print("\n❌ Belirtilen ürün sepetinizde bulunamadı!")
            
        elif choice == "3":
            if not cart.items:
                print("\n❌ Sepetiniz boş!")
            else:
                print("\n=== SEPETİNİZDEKİ ÜRÜNLER ===")
                cart.display_cart()
                print("-"*40)
                print(f"Toplam Tutar: {cart.get_total()} TL")
            
        elif choice == "4":
            if not cart.items:
                print("\n❌ Sepetiniz boş! Sipariş oluşturulamadı.")
            else:
                order = Order(customer, cart)
                order.place_order()
                cart = Cart()  # Yeni boş sepet oluştur
            
        elif choice == "5":
            print("\nBizi tercih ettiğiniz için teşekkürler!")
            print("Program sonlandırılıyor...")
            break
            
        else:
            print("\n❌ Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")
        
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()