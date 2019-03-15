<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateProductoRegistro extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('producto_registro', function (Blueprint $table) {
            $table->bigIncrements('id_producto_registro');
            $table->unsignedBigInteger("id_inventario")->nullable(false);
            $table->unsignedBigInteger("id_producto")->nullable(false);
            $table->integer("cantidad")->nullable(false);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('producto_registro');
    }
}
