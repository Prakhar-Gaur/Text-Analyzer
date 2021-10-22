if(process.argv[2] =="addition")
{
    var res = 0;
for (i = 3; i < process.argv.length; i++) {
    res += Number(process.argv[i]);
}
console.log(res);

}
else if(process.argv[2] == "substraction")
{
    var subs = 0;
    if(process.argv.length == 5)
    {
        subs = Number(process.argv[3]) - Number(process.argv[4] );
    
    console.log(subs);
    }
    else
    {
        console.log("Invalid number of inputs! Try again");
    }
}
else if(process.argv[2] =="multiplication")
{
    var res = 1;
for (i = 3; i < process.argv.length; i++) {
    res =  res*Number(process.argv[i]);
}
console.log(res);

}
else if(process.argv[2] == "division")
{
    var res = 0;
    if(process.argv.length == 5)
    {
        res = Number(process.argv[3]) / Number(process.argv[4] );
    
    console.log(res);
    }
    else
    {
        console.log("Invalid number of inputs! Try again");
    }
}
else
{
    console.log("Unsupported operation! Try again with another operation.")
}

