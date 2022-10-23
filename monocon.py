db_client =


db.users.insertMany([
    {name: "vasya", age: 28},
    {name: "vasya1", age: 34},
    {name: "andrey", age: 56},
    {name: "vasya2", age: 28},
    {name: "anton", age: 28},
    {name: "vasya3", age: 44},
    {name: "vasya4", age: 28}
])

db.users.updateMany(
    {},
    {
        $rename: {
            name: "fullname"
        }
    }
)