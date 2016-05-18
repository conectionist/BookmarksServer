/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.bradvault.bookmarksserver.util;

import static com.bradvault.bookmarksserver.util.Database.logger;
import java.sql.CallableStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Dan
 */
public class DatabaseManager {
    protected Database db;

    public DatabaseManager(Database db) {
        this.db = db;
    }
    
    public void saveUser(String username, String password)
    {
        
    }
    
    public void saveLink(String link, String title)
    {
        
    }
    
    public void saveTag(String tag)
    {
        
    }
    
    public void createUserLink(String username, String link)
    {
        
    }
    
    public void createLinkTagAssociation(String link, String tag)
    {
        
    }
    
    public String getPasswordOfUser(String username) throws SQLException
    {
        ResultSet rs = null;
        String password = "";
        
        try
        {            
            CallableStatement stmt = null;
            String query = "{ call get_user_password(?) }";

            stmt = db.getConnection().prepareCall(query);
            stmt.setString(1, username);
            
            rs = stmt.executeQuery();
            
            rs.next();
            password = rs.getString(1);
        }
        finally
        {
            try {
                if (rs != null) {
                    rs.close();
                }
            } catch (SQLException ex) {
                logger.log(Level.WARNING, ex.getMessage(), ex);
            }
        }
        
        return password;
    }
    
    public ArrayList<String> getBookmarksOfUser(String username) throws SQLException
    {
        ArrayList<String> lst = new ArrayList<>();
        
        ResultSet rs = null;
        
        try
        {            
            CallableStatement stmt = null;
            String query = "{ call get_user_bookmarks(?) }";

            stmt = db.getConnection().prepareCall(query);
            stmt.setString(1, "");

            rs = stmt.executeQuery();

            while (rs.next()) {
                 lst.add(rs.getString("link"));
            }
        }
        finally
        {
            try {
                if (rs != null) {
                    rs.close();
                }
            } catch (SQLException ex) {
                logger.log(Level.WARNING, ex.getMessage(), ex);
            }
        }
        
        return lst;
    }
}
