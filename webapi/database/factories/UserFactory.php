<?php

use Faker\Generator as Faker;

$factory->define(Model::class, function (Faker $faker) {
    return [
        //
        password => "passr",
        username => "vendedor01"        
    ];
});
