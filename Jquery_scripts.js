// Textbox validation
if ($('#<%=TxtbxLanguageskills.ClientID %>').val() == "") {
                $('#<%=TxtbxLanguageskills.ClientID %>').addClass('ipalert');
                $('#<%=TxtbxLanguageskills.ClientID %>').focus();
                showErrormsg('Comments not filled', 'bg-red', 0)
                return false;
            }

// Dropdown Validation

 if ($("#<%=DdlLanguage.ClientID%> option:selected").text() == "--Select--") {
                $('#<%=DdlLanguage.ClientID %>').addClass('ipalert');
                $('#<%=DdlLanguage.ClientID %>').focus();
                showErrormsg('Choose Language', 'bg-red', 0)
                return false;
            }

$('#EmbedPDF').attr('src', PdfUrl);

varstring.replace("contains", "hello everyone"); 


