$(function () {
    function exibeHome() {
        $('#home').show()
        $('#planos').hide()
        $('#carros').hide()
    }

    function exibeCarros() {
        $('#carros').show()
        $('#planos').hide()
        //limpa tabela pra por os novos
        $('#corpoTblCarros tr').remove()

        $.ajax({
            url: 'http://localhost:5000/listarCarrosJson',
            method: 'GET',
            dataType: 'json',
            success: preencherTabelaCarros,
            error: function () {
                alert("Falha ao buscar lista de carros");
            }
        });
    }

    function preencherTabelaCarros(Carros) {
        for (var c in Carros) {
            var linhas = `<td>${Carros[c].modelo.marca}</td><td>${Carros[c].modelo.nome}</td><td>${Carros[c].ano}</td><td>${Carros[c].placa}</td><td>${Carros[c].cliente.nome}</td>`
            $('#corpoTblCarros').append(`<tr>${linhas}</tr>`)
        }

        if ($('#corpoTblCarros').children().length <= 0) {
            $('#corpoTblCarros').hide();
            $('#tblCarros').html('<h4>sem carros para listar</h4>').css('text-align', 'center')
        }
    }

    function exibePlanos() {
        $('#planos').show()
        $('#carros').hide()
        //limpa tabela pra por os novos
        $('#corpoTblPlanos tr').remove()

        $.ajax({
            url: 'http://localhost:5000/listarPlanosJson',
            method: 'GET',
            dataType: 'json',
            success: preencherTabelaPlanos,
            error: function () {
                alert("Falha ao buscar lista de planos");
            }
        });
    }

    function exibeClientes() {
        $('#clientes').show()
        $('#carros').hide()
        $('#planos').hide()
        //limpa tabela pra por os novos
        $('#corpoTblClientes tr').remove()

        $.ajax({
            url: 'http://localhost:5000/listarClientesJson',
            method: 'GET',
            dataType: 'json',
            success: preencherTabelaClientes,
            error: function () {
                alert("Falha ao buscar lista de clientes");
            }
        });
    }

    function preencherTabelaPlanos(Planos) {
        for (var c in Planos) {
            var linhas = `<td>${Planos[c].nome}</td>`
            $('#corpoTblPlanos').append(`<tr>${linhas}</tr>`)
        }

        if ($('#corpoTblPlanos').children().length <= 0) {
            $('#corpoTblPlanos').hide();
            $('#tblPlanos').html('<h4>sem planos para listar</h4>').css('text-align', 'center')
        }
    }

    function preencherTabelaClientes(Clientes) {
        for (var c in Clientes) {
            var linhas = `<td>${Clientes[c].nome}</td> `
            $('#corpoTblPlanos').append(`<tr>${linhas}</tr>`)

            //preencher select de planos no modal de edição
            $('#selectPlanos').append(`<option value='${Clientes[c].plano.Id}'>${Clientes[c].plano.nome}</option>`);
        }

        if ($('#corpoTblPlanos').children().length <= 0) {
            $('#corpoTblPlanos').hide();
            $('#tblPlanos').html('<h4>sem planos para listar</h4>').css('text-align', 'center')
        }
    }

    $(document).on("click", "#btnListarCarros", function () {
        exibeCarros();
    });
    $(document).on("click", "#btnListarPlanos", function () {
        exibePlanos();
    });

    $(document).on("click", "#linkInicio", function () {
        exibeHome(); 
    });

    $.ajax({
        url: 'http://localhost:5000/listarClientesJson',
        method: 'GET',
        dataType: 'json',
        success: function clientes(Clientes) {            
            for (var c in Clientes) {
                //preencher select com os clientes cadastradas
                $('#selectCliente').append(`<option value='${Clientes[c].id}'>${Clientes[c].nome}</option>`);
            }
        },
        error: function () {
            alert("Falha ao buscar lista de Clientes");
        }
    });

    $.ajax({
        url: 'http://localhost:5000/listarModelosJson',
        method: 'GET',
        dataType: 'json',
        success: function clientes(Modelos) {            
            for (var m in Modelos) {
                //preencher select com os clientes cadastradas
                $('#selectModelo').append(`<option value='${Modelos[m].id}'>${Modelos[m].nome}</option>`);
            }
        },
        error: function () {
            alert("Falha ao buscar lista de Modelos");
        }
    });

    $(document).on("click", "#btnInserirCarro", function () {
        ano = $("#txtAno").val();
        clienteId = $("#selectCliente").find(":selected").val();
        modeloId = $("#selectModelo").find(":selected").val();
        placa = $("#txtPlaca").val();
        var dados = JSON.stringify({
            ano: ano,
            modeloId: modeloId,
            clienteId: clienteId,
            placa: placa
        });
        $.ajax({
            url: 'http://localhost:5000/incluir_carro',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: exibeCarros,
            error: function () {
                alert("Falha ao salvar novo carro");
            }
        });
    });
    $(document).on("click", "#btnInserirPlano", function () {
        nome = $("#txtNomePlano").val();
        var dados = JSON.stringify({
            nome: nome
        });
        $.ajax({
            url: 'http://localhost:5000/incluir_plano',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: exibePlanos,
            error: function () {
                alert("Falha ao salvar novo plano");
            }
        });
    });

});