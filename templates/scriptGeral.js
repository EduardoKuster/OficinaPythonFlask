$(function() {   
function exibeHome(){
    $('#home').show()
    $('#planos').hide()
    $('#carros').hide()
}

function exibeCarros(){
    $('#carros').show()
    $('#planos').hide()
    //limpa tabela pra por os novos
    $('#corpoTblCarros tr').remove()

    $.ajax({
        url: 'http://localhost:5000/listarCarrosJson',
        method: 'GET',
        dataType: 'json', 
        success: preencherTabelaCarros,
        error: function() {
            alert("Falha ao buscar lista de carros");
        }
    });
}

    function preencherTabelaCarros (Carros) {       
        for (var c in Carros) { 
            var linhas = `<td>${Carros[c].marca}</td><td>${Carros[c].modelo}</td><td>${Carros[c].ano}</td><td>${Carros[c].placa}</td>`
            $('#corpoTblCarros').append(`<tr>${linhas}</tr>`)
        }
        
        if($('#corpoTblCarros').children().length <= 0){
            $('#corpoTblCarros').hide();
            $('#tblCarros').html('<h4>sem carros para listar</h4>').css('text-align', 'center')
        }    
    } 
    function exibePlanos(){
        $('#planos').show()
        $('#carros').hide()
        //limpa tabela pra por os novos
        $('#corpoTblPlanos tr').remove()
    
        $.ajax({
            url: 'http://localhost:5000/listarPlanosJson',
            method: 'GET',
            dataType: 'json', 
            success: preencherTabelaPlanos,
            error: function() {
                alert("Falha ao buscar lista de planos");
            }
        });
    }
    
        function preencherTabelaPlanos (Planos) {     
            for (var c in Planos) { 
                var linhas = `<td>${Planos[c].nome}</td>`
                $('#corpoTblPlanos').append(`<tr>${linhas}</tr>`)
            }
            
            if($('#corpoTblPlanos').children().length <= 0){
                $('#corpoTblPlanos').hide();
                $('#tblPlanos').html('<h4>sem planos para listar</h4>').css('text-align', 'center')
            }    
        } 

    $(document).on("click", "#btnListarCarros", function() { 
             exibeCarros(); 
           }); 
           $(document).on("click", "#btnListarPlanos", function() { 
            exibePlanos(); 
          }); 
         
           $(document).on("click", "#linkInicio", function() { 
              exibeHome(); //mostrar modal de página de inicio??
           });

           $(document).on("click", "#btnInserirCarro", function() { 
                  ano = $("#txtAno").val(); 
                  marca = $("#txtMarca").val(); 
                  modelo = $("#txtModelo").val(); 
                  placa = $("#txtPlaca").val(); 
                  var dados = JSON.stringify({ ano: ano, marca: marca, modelo: modelo, placa: placa}); 
                  $.ajax({ 
                     url: 'http://localhost:5000/incluir_carro', 
                     type: 'POST', 
                     dataType: 'json', 
                     contentType: 'application/json', 
                     data: dados,
                     success: exibeCarros,
                     error: function() {
                        alert("Falha ao salvar novo carro");
                    }
                  });
                });
                $(document).on("click", "#btnInserirPlano", function() { 
                    nome = $("#txtNomePlano").val(); 
                    var dados = JSON.stringify({ nome: nome}); 
                    $.ajax({ 
                       url: 'http://localhost:5000/incluir_plano', 
                       type: 'POST', 
                       dataType: 'json', 
                       contentType: 'application/json', 
                       data: dados,
                       success: exibePlanos,
                       error: function() {
                          alert("Falha ao salvar novo plano");
                      }
                    });
                  });
                
});
