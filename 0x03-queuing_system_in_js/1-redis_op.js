#!/usr/bin/yarn dev
import createClient from 'redis'

const client =  createClient()

client.on("error", (error)=> {
    console.log('Redis client connected to the server:',error.toString());
});
client.on('connect', () => {
    console.log("Redis client connected to the server");
});

let setNewSchool = (schoolName, value) => {
    client.SET(schoolName, value, print);
};

let displaySchoolValue = (schoolName) => {
    client.GET(schoolName, (_err, reply) => {
        console,log(reply);
    });
};
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
