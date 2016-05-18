<%-- 
    Document   : 401
    Created on : May 14, 2016, 8:35:07 PM
    Author     : Dan
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
    <title>401 - Authorization required</title>
    <%
        String missing_parameter = (String)request.getAttribute("missing_parameter");
        String invalid_parameter = (String)request.getAttribute("invalid_parameter");
        
        if(missing_parameter != null)
        {
    %>
    
        <h2><%= missing_parameter.toString() %> is missing</h2>
    
    <% } else if(invalid_parameter != null) { %>
    
        <h2><%= invalid_parameter.toString() %> is invalid</h2>
    
    <%    
    } else {
    %>
        <h2> Who be yee? </h2>
    <% } %>
</html>
