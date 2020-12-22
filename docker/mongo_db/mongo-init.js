db.createUser({
    user: 'root',
    pwd: 'root',
    roles: [
        {
            role: 'readWrite',
            db: 'database'
        },
        {
            role: 'readWrite',
            db: 'database'
        },
        {
            role: 'root',
            db: 'admin'
        }
    ]
})