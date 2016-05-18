/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.bradvault.bookmarksserver.servlets;

import com.bradvault.bookmarksserver.util.Database;
import com.bradvault.bookmarksserver.util.DatabaseManager;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;
import java.util.ArrayList;
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
public class BookmarksServlet extends HttpServlet {

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
        
        boolean isAuthenticated = false;
        
        Cookie[] cookies = request.getCookies();
        
        if(cookies != null)
        {
            for(Cookie c : cookies)
            {
                if(c.getName().equals("username"))
                {
                    isAuthenticated = true;
                    break;
                }
            }
        }
        
        
        if(!isAuthenticated)
        {
            RequestDispatcher view = null;
            view = request.getRequestDispatcher("401.jsp");
            view.forward(request, response);
            return;
        }
        
        ArrayList<String> bookmarks = new ArrayList<>();
        
        try {
            bookmarks = dbmgr.getBookmarksOfUser("");
            
        } catch (SQLException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Your bookmarks</title>");            
            out.println("</head>");
            out.println("<body>");
            
            for (String bookmark : bookmarks) {
                out.println("<h4>" + bookmark + "</h4>");
            }
            
            out.println("</body>");
            out.println("</html>");
        }
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
