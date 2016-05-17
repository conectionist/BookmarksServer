/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.bradvault.bookmarksserver.servlets;

import Exceptions.InvalidParameterException;
import Exceptions.MissingParameterException;
import java.io.IOException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Dan
 */
public class AuthServlet extends HttpServlet {

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
            view = request.getRequestDispatcher("welcome.html");
        }
        catch(MissingParameterException ex)
        {
            request.setAttribute("missing_parameter", ex.getMissingParameterName());
            view = request.getRequestDispatcher("401.jsp");
        }
        catch(InvalidParameterException ex)
        {
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
        //throw new InvalidParameterException();
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
