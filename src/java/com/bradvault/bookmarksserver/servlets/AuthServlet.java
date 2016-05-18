/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.bradvault.bookmarksserver.servlets;

import Exceptions.InvalidParameterException;
import Exceptions.MissingParameterException;
import com.bradvault.bookmarksserver.util.Database;
import com.bradvault.bookmarksserver.util.DatabaseManager;
import java.io.IOException;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Dan
 */
public class AuthServlet extends HttpServlet {

    protected DatabaseManager dbmgr;

    @Override
    public void init(ServletConfig config) throws ServletException {
        super.init(config);

        try {
            Database db = new Database("localhost", 3306, "ionica", "parola", "bookmarks");

            dbmgr = new DatabaseManager(db);
        } catch (SQLException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        
        RequestDispatcher view = null;
        
        try
        {
            validateParams(request);
            verifyParams(request);
            request.setAttribute("username", request.getParameter("username"));
            view = request.getRequestDispatcher("welcome.jsp");
            
            Cookie cookie = new Cookie("username", request.getParameter("username"));
            cookie.setMaxAge(30 * 1);
            response.addCookie(cookie);
        }
        catch(MissingParameterException ex)
        {
            request.setAttribute("missing_parameter", ex.getMissingParameterName());
            view = request.getRequestDispatcher("401.jsp");
        }
        catch(InvalidParameterException ex)
        {
            request.setAttribute("invalid_parameter", ex.getInvalidParameterName());
            view = request.getRequestDispatcher("401.jsp");
        }
        
        view.forward(request, response);
    }
    
    protected void validateParams(HttpServletRequest request) 
            throws MissingParameterException
    {
        String username = request.getParameter("username");
        
        if(username == null)
            throw new MissingParameterException("username");
        
        String password = request.getParameter("password");
        
        if(password == null)
            throw new MissingParameterException("password");
    }
    
    protected void verifyParams(HttpServletRequest request) 
            throws InvalidParameterException
    {
        String user = request.getParameter("username");
        String request_password = request.getParameter("password");
        
        String password = "";
        
        try {
            password = dbmgr.getPasswordOfUser(user);
            
        } catch (SQLException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        if (password.isEmpty())
            throw new InvalidParameterException("username");
        
        if(!password.equals(request_password))
            throw new InvalidParameterException("password");
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
