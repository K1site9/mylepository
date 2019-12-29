    $(function(){
        var countId = 1
        $("#content h2,#content h3").each(function(){
            var ttl = $(this).text();
            var lv = this.nodeName.toLowerCase();
            this.id = 'ttl-' + countId;
            countId ++;
            $("#index").append('<dd class="lv_'+lv+'"><a href="#'+this.id+'">'+ttl+'</a></dd>');
        });
    });