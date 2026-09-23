import {PrismaClient} from "@prisma/client";
const db=new PrismaClient();
async function main(){await db.user.create({data:{name:"Pranaya Simkhada",email:"workwithpranayaa@gmail.com",role:"admin"}});await db.activity.createMany({data:[{title:"Demo workspace created",detail:"Portfolio seed data is ready."},{title:"System check passed",detail:"API and database configuration loaded."}]});}
main().finally(()=>db.$disconnect());