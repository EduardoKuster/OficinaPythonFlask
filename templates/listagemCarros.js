$(function() { 

    $.ajax({
        url: 'http://localhost:5000/listarCarrosJson',
        method: 'GET',
        dataType: 'json', 
        success: preencherTabela,
        error: function() {
            alert("Falha ao buscar lista de carros");
        }
    });

    function preencherTabela (Carros) {       
        for (var c in Carros) { 
            var linhas = `<td>${Carros[c].marca}</td><td>${Carros[c].modelo}</td><td>${Carros[c].ano}</td><td>${Carros[c].placa}</td>`
            $('#corpoTblCarros').append(`<tr>${linhas}</tr>`)
        }
        
        if($('#corpoTblCarros').children().length <= 0){
            $('#corpoTblCarros').hide();
            $('#tblCarros').html('<h4>sem carros para listar</h4>').css('text-align', 'center')
        }    
    } 
});

