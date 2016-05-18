<%-- 
    Document   : 401
    Created on : May 14, 2016, 8:35:07 PM
    Author     : Dan
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
    <title>Authenticated</title>
    <%
        String username = (String)request.getAttribute("username");
        
        if(username != null)
        {
    %>
    
        <h2>Welcome, <%=username.toString()%>!</h2>
    
    <% } %>
</html>
