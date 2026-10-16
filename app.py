# Real Proof of Concept: Document Database (MongoDB with Docker)
# Author: Nourah Nassir
# Project: Database Alternative Data Models: Beyond Relational

from pymongo import MongoClient

def run_document_db_poc():
    # 1. الاتصال بقاعدة البيانات التي تعمل داخل حاوية Docker
    # (المنفذ الافتراضي لـ MongoDB هو 27017)
    client = MongoClient("mongodb://localhost:27017/")
    
    # اختيار قاعدة البيانات والمجموعة (Collection)
    db = client["holberton_alternative_db"]
    collection = db["articles"]

    # تنظيف البيانات القديمة للاختبار النظيف
    collection.delete_many({})
    print("[INFO] Connected to MongoDB Docker container successfully.\n")

    # 2. CREATE: إدخال مستند حقيقي مع ميزة الهيكل المرن والمستندات المتداخلة (Nested Documents)
    article_document = {
        "title": "Introduction to Document Databases",
        "author": "Nourah Nassir",
        "tags": ["nosql", "mongodb", "polyglot-persistence"],
        "metadata": {
            "views": 250,
            "status": "published",
            "category": "Database Engineering"
        }
    }
    
    insert_result = collection.insert_one(article_document)
    print(f"[CREATE] Inserted document with ID: {insert_result.inserted_id}")

    # 3. READ: الاستعلام عن المستند والبحث داخل الحقول
    print("\n[READ] Querying document by author...")
    found_doc = collection.find_one({"author": "Nourah Nassir"})
    print("Found Document:", found_doc)

    # 4. UPDATE: تحديث حقل داخل المستند باستخدام عوامل MongoDB ($set)
    print("\n[UPDATE] Updating article title...")
    update_result = collection.update_one(
        {"author": "Nourah Nassir"},
        {"$set": {"title": "Advanced Document Databases & NoSQL Architecture"}}
    )
    print(f"[UPDATE] Modified count: {update_result.modified_count}")
    
    # عرض المستند بعد التحديث
    updated_doc = collection.find_one({"author": "Nourah Nassir"})
    print("Updated Document Title:", updated_doc.get("title"))

    # 5. DELETE: حذف المستند عند انتهاء التجربة
    print("\n[DELETE] Cleaning up test document...")
    delete_result = collection.delete_one({"author": "Nourah Nassir"})
    print(f"[DELETE] Deleted count: {delete_result.delete_count}")

    # إغلاق الاتصال
    client.close()
    print("\n[INFO] POC execution completed successfully!")

if __name__ == "__main__":
    run_document_db_poc()
